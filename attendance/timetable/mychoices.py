CONFERENCE = 'Conference'
TRAINING = 'Training'
WORKSHOP = 'Workshop'
MEETING = 'Meeting'
TYPE_OF_EVENT_CHOICES = (
        (CONFERENCE, 'Conference'),
        (TRAINING, 'Training'),
        (WORKSHOP, 'Workshop'),
        (MEETING, 'Meeting'),
)

C3 = 'C3'
CIRCL = 'CIRCL'
CASES = 'CASES'
DEPARTMENT_CHOICES = (
        (C3, 'C3'),
        (CIRCL, 'CIRCL'),
        (CASES, 'CASES'), 
)

HALF = '4 hours'
ONE = '8 hours'
ONENHALF = '12 hours'
TWO = '16 hours'
TWONHALF = '20 hours'
THREE = '24 hours'
DURATION_CHOICES = (
        (HALF, '4 hours'),
        (ONE, '8 hours'),
        (ONENHALF, '12 hours'),
        (TWO, '16 hours'),
        (TWONHALF, '20 hours'),
        (THREE, '24 hours'),
)

SPEAKER = 'Speaker'
ATTENDEE = 'Attendee'
ACTIVITY_TYPE_CHOICES = (
        (SPEAKER, 'Speaker'),
        (ATTENDEE, 'Attendee'),
)