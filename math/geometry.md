# Geometry

## Similar triangles

Given two triangles $ABC$ and $DEF$.

<svg width="300" height="200" style="font-family: 'LatinModern'" font-style="italic" xmlns="http://www.w3.org/2000/svg">
  <!-- Triangle ABC -->
  <polygon points="50,150 70,100 120,150" 
           fill="none" stroke="green" stroke-width="2"/>
  <circle cx="50" cy="150" r="2" fill="black" />
  <circle cx="70" cy="100" r="2" fill="black" />
  <circle cx="120" cy="150" r="2" fill="black" />
  <text x="45" y="165" font-size="12" fill="green">A</text>
  <text x="65" y="95" font-size="12" fill="green">B</text>
  <text x="115" y="165" font-size="12" fill="green">C</text>
  <!-- Triangle DEF -->
  <polygon points="150,150 180,70 250,150" 
           fill="none" stroke="green" stroke-width="2"/>
  <circle cx="150" cy="150" r="2" fill="black" />
  <circle cx="180" cy="70" r="2" fill="black" />
  <circle cx="250" cy="150" r="2" fill="black" />
  <text x="145" y="165" font-size="12" fill="green">D</text>
  <text x="175" y="65" font-size="12" fill="green">E</text>
  <text x="245" y="165" font-size="12" fill="green">F</text>
</svg>

Triangles are called similar ($\Delta ABC \sim \Delta EDF$) if the following holds:

$$\frac{AB}{DE} = \frac{AC}{DF} = \frac{BC}{EF}$$

and

$$\angle A = \angle D, \quad \angle B = \angle E, \quad \angle C = \angle F.$$

The value

$$k = \frac{P_{ABC}}{P_{DEF}}$$

is called the **coefficient of similarity**, where:
- $P_{ABC}$ is the perimeter of triangle $ABC$.
- $P_{DEF}$ is the perimeter of triangle $DEF$.

For coefficient of similarity is a fair expression:

$$k^2=\frac{S_{ABC}}{S_{DEF}}$$

Where:

- $S_{ABC}$ is the area of triangle $ABC$.
- $S_{DEF}$ is the area of triangle $DEF$.


## Median

Median is a line segment that connects a vertex to the midpoint of the opposite side.

The following picture illustrates the median $AO$ of the $\angle BAC$.

<svg width="400" height="400" viewBox="-5 80 120 150" fill="black" font-size="10" style="font-family: 'LatinModern'" font-style="italic" text-anchor="middle" xmlns="http://www.w3.org/2000/svg">
  <!-- Triangle ABC -->
  <polygon points="5,150 25,100 75,150" 
           fill="none" stroke="green" stroke-width="2"/>
  <line x1="5" y1="150" x2="50" y2="125" stroke-width="1" stroke="red"/>
  <g stroke-width="0.5" stroke="black">
    <line x1="60" y1="140" x2="65" y2="135"/>
    <line x1="35"  y1="115" x2="40" y2="110"/>
  </g>
  <circle cx="5" cy="150" r="2"/>
  <circle cx="25" cy="100" r="2"/>
  <circle cx="75" cy="150" r="2"/>
  <circle cx="50" cy="125" r="2"/>
  <text x="2" y="160">A</text>
  <text x="25" y="95">B</text>
  <text x="75" y="160">C</text>
  <text x="45" y="138">O</text>
  <text x="27" y="134" fill="red">M</text>
  <g fill="green">
    <text x="40" y="157">a</text>
    <text x="10" y="125">b</text>
    <text x="53" y="123">c</text>
  </g>
  <path d="M 10 140 A 10,10 0,0 1 15,149" fill="none" stroke-width="0.5" stroke="blue"/>
  <text x="15" y="140" fill="blue">γ</text>
</svg>

In the picture, $AC$ is denoted as $M$ for the convenience of the following mathematical descriptions. 

To calculate the distance of the median use formulas:

- $M=\frac{1}{2}\sqrt{2a^2+2b^2-c^2}$.
- $M=\frac{1}{2}\sqrt{2a^2+2b^2+2ab\,cos(\gamma)}.$