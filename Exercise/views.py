from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercise
from .forms import ExerciseForm
from django.contrib.auth.decorators import login_required

@login_required
def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'Exercise/exercise_list.html', {'exercises': exercises})
@login_required
def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    return render(request, 'Exercise/exercise_detail.html', {'exercise': exercise})
@login_required
def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'Exercise/exercise_form.html', {'form': form})
@login_required
def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_detail', pk=exercise.pk)
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'Exercise/exercise_form.html', {'form': form})