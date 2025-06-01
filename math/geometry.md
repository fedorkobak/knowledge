# Geometry

**Geometry is the art of understanding space.**
It’s the branch of mathematics that explores the shapes, sizes, patterns, and positions of objects—from the perfectly round orbit of a planet to the sharp angles of a city skyline. Whether it’s mapping the universe or designing a garden, geometry helps us decode the structure of the world and imagine new ones.

## Triangle

Triangle is a geometric figure with three sides.

The following picture shows example triangle.

<svg width="360" height="300" viewBox="-5 0 120 100" fill="black" font-size="10" style="font-family: 'LatinModern'" font-style="italic" text-anchor="middle" xmlns="http://www.w3.org/2000/svg">
  <polygon points="5,70 25,20 75,70" 
           fill="none" stroke="green" stroke-width="2"/>
  <circle cx="5" cy="70" r="2"/>
  <circle cx="25" cy="20" r="2"/>
  <circle cx="75" cy="70" r="2"/>
  <text x="2" y="80">A</text>
  <text x="25" y="15">B</text>
  <text x="75" y="80">C</text>
</svg>

Check the [specific page](geometry/trianle.md) for more information.

## Parallelogram

A parallelogram is a geometric figure with four sides, where both pairs of opposite sides are parallel.

In the next picture $ABCD$ is a parallelogram, where $AB \parallel CD, AD \parallel CD$.

<svg width="750" height="270" viewBox="-5 -20 250 90" fill="black" font-size="10" style="font-family: 'LatinModern'" font-style="italic" text-anchor="middle" xmlns="http://www.w3.org/2000/svg">
  <polygon points="5,50 35,0 135,0 105,50" 
           fill="none" stroke="green" stroke-width="2"/>
  <circle cx="5" cy="50" r="2"/>
  <circle cx="35" cy="0" r="2"/>
  <circle cx="135" cy="0" r="2"/>
  <circle cx="105" cy="50" r="2"/>
  <text x="2" y="60">A</text>
  <text x="35" y="-5">B</text>
  <text x="135" y="-5">C</text>
  <text x="105" y="60">D</text>
</svg>

## Cone

A cone is a geometric figure formed by a elliptical base. Each point on the base is connected by a straight line to a single point called the **apex** or **vertex**. These lines are called **generating lines**. The perpendicular from the apex to the base of the cone is called the **heigth** of the cone.

The following cell illustrates cone.

<svg width="270" height="290" viewBox="-10 -10 270 290" fill="black" font-size="30" style="font-family: 'LatinModern'" font-style="italic" text-anchor="middle" xmlns="http://www.w3.org/2000/svg">
  <g fill="none" stroke="black" stroke-width="4">
    <path d="M 10 220 L 200 20 250 220 A 100 35 0 0 1 10 220" />
    <path d="M 250 220 A 100 35 0 0 0 17 220" stroke-dasharray="7"/>
  </g>
  <line x1="200" y1="20" x2="40" y2="250" stroke="red" stroke-width="2" />
  <text x="35" y="275">M</text>
  <text x="200" y=15>S</text>
  <text x="100" y="150" fill="red">l</text>
  <circle cx="130" cy="220" r=3 />
  <text x="130" y="210">O</text>
  <g stroke-width="2" stroke-dasharray="7">
    <line x1="130" y1="220" x2="14" y2="220" stroke="green" />
    <line x1="130" y1="220" x2="130" y2="260" stroke="blue" />
    <line x1="130" y1="220" x2="250" y2="220" stroke="black" />
    <line x1="200" y1="20" x2="200" y2="220" stroke="purple" />
  </g>
  <text x="140" y="245" fill="blue">r</text>
  <text x="80" y="215" fill="green">r'</text>
  <text x="190" y="150" fill="purple">h</text>
  <path d="M 200 205 L 185 205 185 220" fill="none" stroke="black" stroke-width="2" />
  <text x="190" y="245">Q</text>
  <circle cx="200" cy="220" r="3" />
<svg>

Here:

- The base is the ellipce with $O$ center and radiuses $r$ and $r'$.
- The apex is $S$.
- The $SM=l$ is a one of the generating lines.
- The $SQ=h$ is the height of the cone.
