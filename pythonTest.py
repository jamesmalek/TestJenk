import matplotlib.pyplot as plt
from ansi2html import Ansi2HTMLConverter

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Plot')

# Convert Matplotlib output to HTML
converter = Ansi2HTMLConverter()
html_output = converter.convert(plt.gcf()._repr_html_())
print(html_output)
