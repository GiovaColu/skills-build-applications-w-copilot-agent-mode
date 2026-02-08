from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write('Creating users...')
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team=marvel, is_leader=True),
            User(email='captain@marvel.com', name='Captain America', team=marvel),
            User(email='spiderman@marvel.com', name='Spider-Man', team=marvel),
            User(email='batman@dc.com', name='Batman', team=dc, is_leader=True),
            User(email='superman@dc.com', name='Superman', team=dc),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team=dc),
        ]
        for user in users:
            user.save()

        self.stdout.write('Creating workouts...')
        workouts = [
            Workout(name='Strength Training', description='Build muscle and strength', suggested_for='Marvel'),
            Workout(name='Speed Run', description='Improve speed and agility', suggested_for='DC'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2026-02-01')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2026-02-02')
        Activity.objects.create(user=users[3], type='Swimming', duration=60, date='2026-02-03')
        Activity.objects.create(user=users[4], type='Yoga', duration=40, date='2026-02-04')

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team=marvel, points=120)
        Leaderboard.objects.create(team=dc, points=110)

        self.stdout.write('Ensuring unique index on email...')
        db = connection.cursor().db_conn.client['octofit_db']
        db['octofit_tracker_user'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
