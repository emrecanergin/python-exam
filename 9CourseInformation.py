roomNumbers = {
    'CS101': 3004, 
    'CS102': 4501, 
    'CS103': 6755, 
    'NT110':1244,
    'CM241':1411
    }
roomNumbersDict = dict({'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110':1244,'CM241':1411})

instructor = {'CS101': 'Haynes', 
         'CS102': 'Alvarado', 
         'CS103': 'Rich', 
         'NT110':'Burke',
         'CM241':'Lee'
         }

instructorDict = dict({'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110':'Burke','CM241':'Lee'})

meetingTime = {'CS101': '8:00 a.m.', 
         'CS102': '9:00 a.m.', 
         'CS103': '10:00 a.m.', 
         'NT110':'11:00 a.m.',
         'CM241':'1:00 p.m'
         }

meetingTimeDict = dict({'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110':'11:00 a.m.','CM241':'1:00 p.m'})

cname = str(input('enter course name'))
print('Room number is : ' + str(roomNumbers.get(cname)))
print('Instructor is : ' + str(instructor.get(cname)))
print('Meeting Time is : ' + str(meetingTime.get(cname)))

