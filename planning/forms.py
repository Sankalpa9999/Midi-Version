# planning/forms.py

from django import forms
from .models import WorkoutPlan, WorkoutSession, ScheduledWorkout

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['exercise', 'description']

class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ['exercise', 'sets', 'reps', 'duration', 'rest_interval']

class ScheduledWorkoutForm(forms.ModelForm):
    class Meta:
        model = ScheduledWorkout
        fields = ['workout_plan', 'date']
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }