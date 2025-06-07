# Triangle

A triangle is a geometric figure with three sides. This page explores the various properties of triangles.

## Similar triangles

Given two triangles $ABC$ and $DEF$.

<svg
width="500" height="200"
style="font-family: 'LatinModern'" font-style="italic"
fill="black" stroke="black"
xmlns="http://www.w3.org/2000/svg">
  <g fill="none" stroke-width="2">
    <polygon points="20,170 60,70 150,170" />
    <polygon points="200,170 260,30 380,170" />
    </g>
    <g font-size="22" stroke="none">
    <text x="10" y="190" >A</text>
    <text x="55" y="60" >B</text>
    <text x="145" y="190" >C</text>
    <text x="190" y="190" >D</text>
    <text x="255" y="20" >E</text>
    <text x="375" y="190" >F</text>
    </g>
    <circle cx="20" cy="170" r="3" />
    <circle cx="60" cy="70" r="3" />
    <circle cx="150" cy="170" r="3" />
    <circle cx="200" cy="170" r="3" />
    <circle cx="260" cy="30" r="3" />
    <circle cx="380" cy="170" r="3" />
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

<svg
  width="360" height="320"
  viewBox="-5 -15 90 80"
  fill="black" font-size="10"
  style="font-family: 'LatinModern'" font-style="italic"
  text-anchor="middle"
  xmlns="http://www.w3.org/2000/svg">
    <polygon
      points="5,50 25,0 75,50"
      fill="none"
      stroke="black"
      stroke-width="1"
    />
    <line x1="5" y1="50" x2="50" y2="25" stroke-width="1" stroke="red"/>
    <g stroke-width="0.5" stroke="black">
      <line x1="60" y1="40" x2="65" y2="35"/>
      <line x1="35"  y1="15" x2="40" y2="10"/>
    </g>
    <circle cx="5" cy="50" r="1"/>
    <circle cx="25" cy="0" r="1"/>
    <circle cx="75" cy="50" r="1"/>
    <circle cx="50" cy="25" r="1"/>
    <text x="2" y="60">A</text>
    <text x="25" y="-5">B</text>
    <text x="75" y="60">C</text>
    <text x="50" y="35">O</text>
    <text x="27" y="34" fill="red">m</text>
    <g fill="black">
      <text x="40" y="57">a</text>
      <text x="10" y="25">b</text>
      <text x="53" y="23">c</text>
    </g>
    <path d="M 8 43 A 7,7 0,0 1 13,50" fill="none" stroke-width="0.5" stroke="blue"/>
    <text x="14" y="42" fill="blue">γ</text>
</svg>

In the picture, $AC$ is denoted as $M$ for the convenience of the following mathematical descriptions. 

### Distance

To calculate the distance of the median use formulas:

- $m=\frac{1}{2}\sqrt{2a^2+2b^2-c^2}$.
- $m=\frac{1}{2}\sqrt{2a^2+2b^2+2ab\,\cos(\gamma)}.$

To prove identity $M=\frac{1}{2}\sqrt{2a^2+2b^2-c^2}$ extend the paralellogramm, as showen at the following picutre:

<svg
  width="440" height="320"
  viewBox="-5 -15 110 80"
  fill="black" font-size="10"
  style="font-family: 'LatinModern'" font-style="italic"
  text-anchor="middle"
  xmlns="http://www.w3.org/2000/svg">
    <polygon
      points="5,50 25,0 75,50"
      fill="none"
      stroke="black"
      stroke-width="1"
    />
    <line x1="5" y1="50" x2="50" y2="25" stroke-width="1" stroke="red"/>
    <g stroke-width="0.5" stroke="black">
      <line x1="60" y1="40" x2="65" y2="35"/>
      <line x1="35"  y1="15" x2="40" y2="10"/>
    </g>
    <circle cx="5" cy="50" r="1"/>
    <circle cx="25" cy="0" r="1"/>
    <circle cx="75" cy="50" r="1"/>
    <circle cx="50" cy="25" r="1"/>
    <text x="2" y="60">A</text>
    <text x="25" y="-5">B</text>
    <text x="75" y="60">C</text>
    <text x="50" y="35">O</text>
    <text x="27" y="34" fill="red">m</text>
    <g fill="black">
      <text x="40" y="57">a</text>
      <text x="10" y="25">b</text>
      <text x="53" y="23">c</text>
    </g>
    <g stroke-width="0.7" stroke="black" stroke-dasharray="3">
      <line x1="25" y1="0" x2="95" y2="0"/>
      <line x1="95" y1="0" x2="75" y2="50"/>
      <line x1="95" y1="0" x2="50" y2="25" stroke="red" />
    </g>
    <g stroke-width="0.5" stroke="red">
      <line x1="70.3" y1="10.75" x2="72.85" y2="15.25"/>
      <line x1="74.65" y1="14.25" x2="72.15" y2="9.75"/>
      <line x1="29.65" y1="39.25" x2="27.15" y2="34.75"/>
      <line x1="27.85" y1="40.25" x2="25.35" y2="35.75"/>
    </g>
    <circle cx="95" cy="0" r="1"/>
</svg>
