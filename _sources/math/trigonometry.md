# Trigonometry

Trigonometry is a branch of mathematics that studies the relationships between the angles and sides of triangles, especially right-angled triangles.

## Definition

There are two main ways to define trigonometric functions: the unit sircle method and the right-angled triangle method.

Here’s a corrected and clearer version of your description:

The **unit circle** method uses a circle with a radius of 1 centered at $(0, 0)$. A ray at an angle $\theta$ from the positive $x$-axis extends from the origin. The coordinates of the point where the ray intersects the circle define the trigonometric functions of $\theta$: the $x$-coordinate gives $\cos(\theta)$, and the $y$-coordinate gives $\sin(\theta)$.

The following picture shows a typical unit circle.

<svg width="600" height="600" viewBox="-2 -2 4 4" xmlns="http://www.w3.org/2000/svg">
  <g font-size="0.15" text-anchor="middle" stroke-width="0.02" style="font-family: 'LatinModern'" font-style="italic">
   <line x1="-1.3" y1="0" x2="1.3" y2="0" stroke="black"/>
   <line x1="0" y1="-1.3" x2="0" y2="1.3" stroke="black"/>
   <circle cx="0" cy="0" r="1" fill="none" stroke="black" stroke-width="0.005"/>
   <path d="M 1.3 0.03 L 1.35 0 L 1.3 -0.03 Z" fill="black" stroke="black"/>
   <path d="M 0.03 -1.3 L 0 -1.35 L -0.03 -1.3 Z" fill="black" stroke="black"/>
   <text x="1.03" y="0.12">1</text>
   <text x="-0.05" y="-1">1</text>
   <line x1="0" y1="0" x2="0.707" y2="-0.707" stroke="red"/>
   <line x1="0.707" y1="-0.707" x2="0" y2="-0.707" stroke="green" stroke-dasharray="0.05"/>
   <text x="-0.2" y="-0.68" fill="green">sin(θ)</text>
   <line x1="0.707" y1="-0.707" x2="0.707" y2="0" stroke="blue" stroke-dasharray="0.05"/>
   <text x="0.707" y="0.14" fill='blue'>cos(θ)</text>
   <text x="0.25" y="-0.06">θ</text>
   <text x="-0.1" y="-1.3">y</text>
   <text x="1.3" y="0.15">x</text>
  </g>
  <path d="M 0.14,-0.14 A 0.2,0.2 0 0,1 0.2,0" fill="none" stroke="black" stroke-width="0.005"/>
</svg>

In the right-angle method, trigonometric functions are defined as the ratios between the sides of a right-angled triangle. For non-right angle of a right-angled triangle:

- Sine is the ratio of the opposite side to the hypotenuse.
- Cosine is the ratio of the adjacent side to the hypotenuse.
- Tangent is the ratio of the opposite and adjacent sides.

The following picture shows $\Delta ABC$ with some notations.


<svg width="400" height="400" viewBox="-0.2 -1 1 1.2"  xmlns="http://www.w3.org/2000/svg" 
stroke="black" style="font-family: 'LatinModern'" font-style="italic" font-size="0.08">
  <g stroke-width="0.01">
    <line x1="0" y1="0" x2="0.5" y2="0" stroke="blue"/>
    <line x1="0" y1="0" x2="0" y2="-0.86" stroke="green"/>
    <line x1="0.5" y1="0" x2="0" y2="-0.86" stroke="red"/>
  </g>
  <g stroke-width="0.001">
    <text x="-0.05" y="0.07">A</text>
    <text x="0.5" y="0.07">B</text>
    <text x="-0.05" y="-0.88">C</text>
    <text x="0.37" y="-0.04">θ</text>
  </g>
  <g stroke-width="0.003" fill="none">
    <path d="M 0,-0.07 L 0.07,-0.07 L 0.07,0"/>
    <path d="M 0.46,-0.07 A 0.07,0.07 0 0,0 0.42,0"/>
  </g>
</svg>

The following statements will be correct according to notations:

- $sin(\theta) = \frac{\textcolor{green}{AC}}{\textcolor{red}{BC}}$.
- $cos(\theta) = \frac{\textcolor{blue}{AB}}{\textcolor{red}{BC}}$.
- $tan(\theta) = \frac{\textcolor{green}{AC}}{\textcolor{blue}{AB}}$.

## Identities

In trigonometry, trigonometric identities are equalities that involve trigonometric functions and are true for every value of the occurring variables for which both sides of the equality are defined.

The table below lists some of the identities.

| **Group**            | **Identity**                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------- |
| **Fundamental**      | $\sin^2 x + \cos^2 x = 1$                                                                 |
|                      | $1 + \tan^2 x = \sec^2 x$                                                                 |
|                      | $1 + \cot^2 x = \csc^2 x$                                                                 |
| **Reciprocal**       | $\sin x = \frac{1}{\csc x}$                                                               |
|                      | $\cos x = \frac{1}{\sec x}$                                                               |
|                      | $\tan x = \frac{1}{\cot x}$                                                               |
|                      | $\cot x = \frac{1}{\tan x}$                                                               |
| **Quotient**         | $\tan x = \frac{\sin x}{\cos x}$                                                          |
|                      | $\cot x = \frac{\cos x}{\sin x}$                                                          |
| **Shift Identities** | $\cos(\frac{\pi}{2} + x) = -\sin(x)$                                                      |
|                      | $\sin(\frac{\pi}{2} + x) = \cos(x)$                                                       |
|                      | $\cos(\pi + x) = -\cos(\pi)$                                                              |
|                      | $\sin(\pi + x) = -\sin(\pi)$                                                              |
|                      | $\cos(\frac{3 \pi}{2} + x) = \sin(x)$                                                     |
|                      | $\sin(\frac{3 \pi}{2} + x) = -\cos(x)$                                                    |
| **Co-Function**      | $\sin(\frac{\pi}{2} - x) = \cos x$                                                        |
|                      | $\tan(\frac{\pi}{2} - x) = \cot x$                                                        |
|                      | $\sec(\frac{\pi}{2} - x) = \csc x$                                                        |
| **Even-Odd**         | $\cos(-x) = \cos x$                                                                       |
|                      | $\sin(-x) = -\sin x$                                                                      |
|                      | $\tan(-x) = -\tan x$                                                                      |
| **Sum & Difference** | $\sin(a \pm b) = \sin a \cos b \pm \cos a \sin b$                                         |
|                      | $\cos(a \pm b) = \cos a \cos b \mp \sin a \sin b$                                         |
|                      | $\tan(a \pm b) = \frac{\tan a \pm \tan b}{1 \mp \tan a \tan b}$                           |
| **Double Angle**     | $\sin 2x = 2 \sin x \cos x$                                                               |
|                      | $\cos 2x = \cos^2 x - \sin^2 x = 2 \cos^2 x - 1 = 1 - 2 \sin^2 x$                         |
|                      | $\tan 2x = \frac{2 \tan x}{1 - \tan^2 x}$                                                 |
| **Half Angle**       | $\sin^2 x = \frac{1 - \cos 2x}{2}$                                                        |
|                      | $\cos^2 x = \frac{1 + \cos 2x}{2}$                                                        |
| **Product-to-Sum**   | $\sin(a)\sin(b) = \frac{1}{2}[\cos(a - b) - \cos(a + b)]$                                 |
|                      | $\cos(a)\cos(b) = \frac{1}{2}[\cos(a - b) + \cos(a + b)]$                                 |
|                      | $\sin(a)\cos(b) = \frac{1}{2}[\sin(a + b) + \sin(a - b)]$                                 |
| **Sum-to-Product**   | $\sin(a) + \cos(b) = 2 \sin\left(\frac{a + b}{2}\right)\cos\left(\frac{a - b}{2}\right)$  |
|                      | $\sin(a) - \sin(b) = 2 \cos\left(\frac{a + b}{2}\right)\sin\left(\frac{a - b}{2}\right)$  |
|                      | $\cos(a) + \cos(b) = 2 \cos\left(\frac{a + b}{2}\right)\cos\left(\frac{a - b}{2}\right)$  |
|                      | $\cos(a) - \cos(b) = -2 \sin\left(\frac{a + b}{2}\right)\sin\left(\frac{a - b}{2}\right)$ |

