
import scoop_wrapper
import matplotlib.pyplot as plt
import numpy as np

scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.9::INSTR")
data = scoop.takemeasurement("CHAN1","NORMal","ASCii")

plt.plot(100,data)
plt.show()
