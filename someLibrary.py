import numpy
import matplotlib
import matplotlib.pyplot

maasListesi = numpy.random.normal(4000, 500, 1000)

print(numpy.mean(maasListesi))

matplot.hist(maasListesi, 50)
matplot.show()