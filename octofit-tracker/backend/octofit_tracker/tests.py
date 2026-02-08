from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(email="test@example.com", name="Test User", team=team)
        self.assertEqual(user.name, "Test User")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(email="test@example.com", name="Test User", team=team)
        activity = Activity.objects.create(user=user, type="Running", duration=30, date="2026-02-08")
        self.assertEqual(activity.type, "Running")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Morning Run", description="Run 5km", suggested_for="Cardio")
        self.assertEqual(workout.name, "Morning Run")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Test Team")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
