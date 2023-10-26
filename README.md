# Projects

This is a collection of the various projects and other small things I have made on my own time. Most were just made for fun or to mess with something I thought was interesting, so they aren't the most complete things I've ever built. All that to say, these aren't really intended to be very user-friendly or interactive where they don't have to be, so handle at your own risk. Where more than just running a file directly is required, instructions will be provided.

## BF Interpreter

I was speaking with a coworker one day and we came upon the topic of esoteric languages and the many ways in which they can be uniquely terrible and funny. This led me to me describing BrainFuck (BF), explaining its lovely personal brand of awfulness, and both of us being interested in seeing it in action. At the time, I was looking into compilers and interpreters and figured this would be a nice, relaxing place to wade into that topic programmatically. 

BFInterpreter is exactly what it says, just feed a text file in with a .bf file extension and it will crunch right through it. Just keep in mind that this isn't meant to help you actually write in BF and will happily allow you to run a program that doesn't terminate or output anything. BFToPF is just a program that converts .bf files to a visual representation using binary RBG values. Read about it when looking at the esoteric languages Wiki and thought it would be funny to implement. Some specifics on my interpeter: memory is a tape of 30000 looping cells, values cannot go below 0 and do not overflow to the maximum, and calling input when there is none will store a 0

Both files are invoked with "python '*python file*' '*.bf file*'"

## Connect 4
The Connect 4 programs were created because I wanted to play with minimaxxing and alpha-beta pruning, and was then prompted to see what I could do to throw a visual component on top. I might come back to this with an attempt to make an agent using AI sometime in the future seeing as I've started to get a better understanding of them.

Put Connect4AIAgent, Connect4Window, and Gameboard in the same directory and run Connect4Window to see the project as it was originally presented. All it does it put together a specific kind of Gameboard instance and setup the minimaxxing algorithm and display it. You will need pygame installed for this. If you want to use the Gameboard class for another game, you will have to create an instance of it for yourself in your code as it will not run on its own.

## Game of Life

When I first started programming I was told to try and make Conway's Game of Life as it's simple to understand and, in theory, implement. Unfortunately for me, I was not good enough yet to really understand how to do much of what I do now and thus failed miserably. I recently started going through some old projects of mine and remembered my last attempt at this. What you see is the result of 2 days of thoroughly dunking on my past self for his lack of skill.

Put both files in the same folder and run GameOfLifeVisual to run this.

## Graphics
These programs come from a class I took on building 3D graphics from scratch in college. They are entirely seperate programs and can be run individually to see the various stages of creation as the project progressed. While I am not entirely happy with how they turned out and could certainly make them so much cleaner and faster knowing what I do now, I thought it was worth archiving as they were part of the most involved and interesting project I undertook at school.

In order of development: Wireframe, InPlaceManipulation, PolygonShading, ShadingModels

## Splines

I often find myself in the mood to just build things and see if I can make it work, and it was on one such occasion that I stumbled across De Casteljau's algorithm. I've never been one for pure math, so the visual aspect of what this algorithm described so beautifully interested me greatly. This led to a rabbit hole of video games, animation, vector graphics, and all sorts of other applications. Ultimately, I ended up implementing the BezierCurve file you see and liked how it looked so much I decided to see what else this thing could do. 

BezierSplines are just multiple curves stapled together, HermiteSplines use vectors to define tangents at the control points but they secretly can be defined by specific implementations of BezierCurves, CardinalSplines are much the same except the vectors are automatically defined, and CatmullRomSplines are just a specific kind of CardinalSpline. All of this from one simple little algorithm... except LinearSplines. Those were just too funny to leave out.

Keep all the files in the same directory and run SplinesVisual for this one, and feel free to mess with the definitions of the splines individually.

## TicTacToe

This program came out of a truly idiotic conversation where I and some coworkers were dicussing the idea that you could make anything if you just wrote enough if statements. Naturally, I wanted to see how far you could push that idea while still making something 'useful' and thus was this stupid thing created. The idea is that it pulls a list of possible boardstates (which I created manually) and the best possible move to make if it appears (which I also did manually) from a text file. It then stores that data and references it when needed instead of running fancy algoithms or any of that other smart nonsense. Not quite the if statement glory it could have been, but the idea is there.

You will need both files in the same folder, or to change the filepath if you run TicTacToe as is. Alternatively, you can implement the class and give it your own dictionary in the format of the original txt file.

## The Chaos Game

I mostly uploaded this just because it was the first project I did at college and it looks cool. No real other reason. Just enjoyed making it and thought to archive it.