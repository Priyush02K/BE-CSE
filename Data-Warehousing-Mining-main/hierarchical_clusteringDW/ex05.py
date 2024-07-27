import matplotlib.pyplot as plt
import numpy as np
#scatter
var_x = np.array([3,7,15,18,29,16,14,28,35,9,21,2,23])
var_y = np.array([90,86,75,146,69,80,89,90,122,76,92,93,99])
plt.scatter(var_x, var_y)
plt.show()

#bar chart
import numpy as np
import matplotlib.pyplot as plt
data = {'cefix':20, 'Cloxacillin':15, 'Paracetamol':30,
'betnsoil':35}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))
plt.bar(courses, values, color ='maroon',
width = 0.4)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

#Pie Chart:-
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Cloxacillin", "betnsoil", "Paracetamol", "cefix"]
plt.pie(y, labels = mylabels)
plt.show()

#Histogram
import matplotlib.pyplot as plt
import numpy as np
var_xi = np.random.normal(170, 10, 250)
plt.hist(var_xi)
plt.show()


