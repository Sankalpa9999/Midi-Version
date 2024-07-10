# planning/views.py

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import WorkoutPlan, WorkoutSession, ScheduledWorkout
from .forms import WorkoutPlanForm, WorkoutSessionForm, ScheduledWorkoutForm
from Dashboard.models import Workout  # Import Workout model
from django.core import serializers

def workout_planner(request):
    workout_plans = WorkoutPlan.objects.filter(user=request.user)
    scheduled_workouts = ScheduledWorkout.objects.filter(user=request.user)
    workouts = Workout.objects.filter(user=request.user)  # Fetch workouts for the calendar
    return render(request, 'planning/workout_planner.html', {
        'workout_plans': workout_plans,
        'scheduled_workouts': scheduled_workouts,
        'workouts': workouts,
    })

def create_workout_plan(request):
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST)
        if form.is_valid():
            workout_plan = form.save(commit=False)
            workout_plan.user = request.user
            workout_plan.save()

            # Retrieve all scheduled workouts associated with this plan
            scheduled_workouts = ScheduledWorkout.objects.filter(workout_plan=workout_plan)

            return render(request, 'planning/workout_planner.html', {
                'workout_plans': WorkoutPlan.objects.filter(user=request.user),
                'scheduled_workouts': scheduled_workouts,
                'workouts': Workout.objects.filter(user=request.user),
            })
    else:
        form = WorkoutPlanForm()
    return render(request, 'planning/create_workout_plan.html', {'form': form})

def add_workout_session(request, plan_id):
    workout_plan = get_object_or_404(WorkoutPlan, id=plan_id)
    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST)
        if form.is_valid():
            workout_session = form.save(commit=False)
            workout_session.workout_plan = workout_plan
            workout_session.save()
            return redirect('workout_planner')
    else:
        form = WorkoutSessionForm()
    return render(request, 'planning/add_workout_session.html', {'form': form, 'workout_plan': workout_plan})

def schedule_workout(request):
    if request.method == 'POST':
        form = ScheduledWorkoutForm(request.POST)
        if form.is_valid():
            scheduled_workout = form.save(commit=False)
            scheduled_workout.user = request.user
            scheduled_workout.save()

            # Serialize only the necessary fields
            serialized_data = {
                'id': scheduled_workout.id,
                'workout_plan': scheduled_workout.workout_plan.exercise.name,  # Assuming name is a field in WorkoutPlan
                'date': scheduled_workout.date.strftime('%Y-%m-%d'),
                # Add other fields as needed
            }

            return redirect('workout_planner')
    else:
        form = ScheduledWorkoutForm()

    return render(request, 'planning/schedule_workout.html', {'form': form})