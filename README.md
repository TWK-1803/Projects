# A note should anyone see this repo besides myself:

Ever since I started archiving these little side projects of mine I've come to realize that a lot of the parts of computer science I once thought impossible - the ones that awed me as a younger programmer - really aren't as unapproachable as they appear. Honestly, I've wanted to mess with some of these topics for a long time, I just never had the motivation to actually find and understand the research before. If anyone sees this, especially if they're a newer programmer, take my advice: try to go a little beyond your depth on each project you do. Obviously, don't try to go straight for the truly impenetrable stuff right away, but don't be afraid to aim for what you think would be really hard, but possible, to do. You'd be surprised just how much you'll be able to do once you've gone through that struggle and prevailed.

What you see here is a collection of the various projects and other small things I have made over time. Most were just made for fun or to mess with something I thought was interesting, so they aren't the most complete things I've ever built. All that to say, these aren't really intended to be very user-friendly or interactive where they don't have to be, so handle at your own risk. Where more than just running a file directly is required, instructions will be provided.

## 24

I played a game when I was younger where you roll 4 dice and try to apply mathematical operations to the numbers you rolled in any order needed to reach the number 24 without changing any of the numbers directly. For example: 1,4,5,6 can reach 24 with 4/(1-5/6). Originally, all that was allowed was +, -, *, /, and (), but there were a few notable cases where the number you rolled could genuinely be unsolvable. This led to adding factorials into the mix once I was old enough to understand them. At some point in college, I proved that just using +, -, *, /, (), and ! was enough to make every possible roll of 4 6-sided dice possible (By exhaustively solving them all by hand as would a true math genius).

Recently, I happened across a program in Haskell that generated these automatically and thought to take a crack at doing that myself. 24_Haskython is the result of my eyeballing the Haskell program (I don't know Haskell... at all) and trying to transpose it into python (failing miserably until things started to line up, apologies for the weirdness). While my truly awful code does tell you what IS possible to solve, it doesnt tell you HOW. 24_Python is something I wrote to automatically make those formulas instead of just spitting out true or false. It definitely isn't as complete or exhaustive as the first program, but it solves my specific use case fine.

Validator is a program I wrote as a sanity check for the generated equations. I tried extending the built-in eval function, but in the end it was simpler to just write my own evalutor. Evaluating infix is hard, so I change the expression into postfix which makes things much easier. I may have gotten carried away a tad and also written a prefix converter and evalutator as well. Oops.

## BF Interpreter

I was speaking with a coworker one day and we came upon the topic of esoteric languages and the many ways in which they can be uniquely terrible and funny. This led me to me describing BrainFuck (BF), explaining its lovely personal brand of awfulness, and both of us being interested in seeing it in action. At the time, I was looking into compilers and interpreters and figured this would be a nice, relaxing place to wade into that topic programmatically. 

BFInterpreter is exactly what it says, just feed a text file in with a .bf file extension and it will crunch right through it. Just keep in mind that this isn't meant to help you actually write in BF and will happily allow you to run a program that doesn't terminate or output anything. BFToPF is just a program that converts .bf files to a visual representation using RBG values. I read about it when looking at the esoteric languages Wiki and thought it would be funny to implement. Some specifics on my interpreter: memory is a tape of 30000 looping cells, values cannot go below 0 and do not overflow to the maximum, and calling input when there is none will store a 0

Both files are invoked with "python '*python file*' '*.bf file*'"

## Boids

Boids are a classic example of complex group behavior emerging from simple rules followed by independent agents—similar to systems like cellular automata. The model was designed to simulate the behavior of animals, such as birds or fish, when they form flocks or schools. The three base rules are surprisingly simple: avoid crowding other agents, align with the average heading of nearby agents, and steer toward the average position of nearby agents.

What makes the simulation so dynamic is that the agents have no knowledge of global information; the rules only apply within a local area around each agent. From there, you can expand the model by adding features like obstacle avoidance or splitting agents into multiple flocks that are attracted to, repulsed by, or indifferent to one another.

Keep all files in the same folder and run BoidsVisual for this one. Feel free to mess with the config options to see what you can make.

## Chaos

Chaos theory is such a strange point of interest for me. I first came across it in a mobile game of all things. Then, recently, I happened across this video: https://www.youtube.com/watch?v=bpGx61xNYhc which got me thinking about it again. There are a lot of chaotic systems out there and a number of them can be found on this website I took the formulae from: https://www.dynamicmath.xyz/strange-attractors/. Really, all that's needed to characterize a chaotic system is extreme sensitivity to input and non-period nature, so it's fitting that some of these come from attempts to model natural phenomena. I did consider making this 3D by allowing rotation of a baked in shape made of generated points, but that turned out to be a little outside my motivation to work on this and it's been a while since I messed with that sort of thing (yes, I can see the Graphics folder and no, that was not recent as of the time of writing for this project). Feel free to mess with the config file (a convention I am coming to like in these side projects of mine) and look at different attractors from whatever perspective you want. Most have an angle that best suits them, but I couldn't be bothered to hard code more than I did when part of the fun is looking at these things for yourself.

Put both files in the same folder and run Attractors to run this.

## Connect 4

The Connect 4 programs were created during an internship I had over the summer because I wanted to play with minimaxxing and alpha-beta pruning and was then prompted to see what I could do to throw a visual component on top by my supervisor. I might come back to this with an attempt to make an agent using ML sometime in the future seeing as I've started to get a better understanding of them.

Put Connect4AIAgent, Connect4Window, and Gameboard in the same directory and run Connect4Window to see the project as it was originally presented. All it does it put together a specific kind of Gameboard instance and setup the minimaxxing algorithm and display it. You will need pygame installed for this. If you want to use the Gameboard class for another game, you will have to create an instance of it for yourself in your code as it will not run on its own.

## Fourier

This project has been floating around in my head for a while ever since I watched 3Blue1Brown's video where he built something that draws arbitrary periodic paths with rotating circles (link for those interested: https://youtu.be/r6sGWTCMz2k?si=sj4fWv18z5q059uH). I had some free time recently and figured I'd take a shot at it and this is the result. It is sort of cheating by using svg files to get the path data, so I might come back at some later date and add the ability to draw anything and have it replicated. Prior to this, I hadn't really ever messed with complex Fourier Series or Fourier Transforms, but it was surprisingly accessible when compared to some of the other stuff I've messed with in this archive. Maybe that's just me getting better at understanding math, or maybe it really isn't as 'complex' as I had originally estimated (please don't judge me for that pun).

I've included an example svg file that works well with the program. Note that the file is made up of one path element and it connects back to itself. Since my interest was with the math, I didn't spend too much time getting something that would work for all svg files. Just keep that in mind if you are messing with this yourself. You will need to have svgpathtools for this to work. Just keep the svg file and the code together and run FourierVisual to get things going.

## Game of Life

When I first started programming, I was told to try and make Conway's Game of Life as it's simple to understand and, in theory, implement. Unfortunately for me, I was not good enough yet to really understand how to do much of what I do now and thus failed miserably. I recently started going through some old projects of mine from all those years ago and remembered my last attempt at this. What you see is the result of 2 days of thoroughly dunking on my past self for his lack of skill.

Put both files in the same folder and run GameOfLifeVisual to run this.

## GJK

Collision detection can be a really hard thing to implement depending on how you approach the problem. Simple shapes like circles and regular polygons have ways you could do it relatively easily in the grand scheme of things, but things get much more difficult with anything more complex. Weirdly enough, I didn't stumble into this project by trying to solve collision detection or anything fancy like that (I love reinventing the wheel as much as any programmer, but even I have limits... occasionally). I actually came across the original academic paper and the beauty of the overarching idea intrigued me. The algorithm was taken practically line for line from Reducible's video on the topic here: https://youtu.be/ajv46BSqcK4?si=NLrF1V4a3sZRvn1i, but I added all the stuff in the background to let it work the way it should directly from the pseudocode (The classic move of stealing the framework and tweaking it to make it do what I want). I know the vector class isn't the usual sort of sloppy, quick implementation only for my personal, objectively ideal, intended use case, but I figured I should make it more robust since I might have uses for it elsewhere. Plus, it's fun to semi-approach stuff the way I do in my day job sometimes - in reasonable, lazy moderation of course since that seems to be the motto for this repo.

Technically this algorithm works for any convex shape, but I went ahead and defined a few simple ones to help test the thing out. Feel free to play with and add on to the Shapes file if you want to make custom blobs of whatever shape you desire.

Keep all files in the same folder and run GJK to get it up and running.

## Graphics

These programs come from a class I took on building 3D graphics from scratch in college. They are entirely separate programs and can be run individually to see the various stages of creation as the project progressed. While I am not entirely happy with how they turned out and could certainly make them so much cleaner and faster knowing what I do now, I thought it was worth archiving as is since they were part of one of the most involved and interesting projects I undertook at school.

In order of development: Wireframe, InPlaceManipulation, PolygonShading, ShadingModels

## ImgToAscii

As much as I like diving down random rabbit holes as my interests change, sometimes it's good to have one of those holes be over and done within a matter of an hour or two rather than the days I spend on other projects. This little thing was inspired, oddly enough, by the works of Petros Vrellis. I played with his techniques and the math behind them for a little while before I decided to see what other stuff might be done to produce an image out of something other than pixels or colors. Eventually, I came across ascii art and put together this program to make some. Normally, I wouldn't put the tiny test scripts or other such experiments I write for these projects in this repo, but the results were too cool looking not to.

The other program is just a slightly code golfed version of the original. A coworker of mine has an interest in code golfing so I thought I'd give it a try myself. Honestly, I kind of enjoy it. Gives me a reason to scratch that optimization itch a little in my personal projects (As if I don't get enough of that in my actual work). I usually don't bother because these are more about me exploring topics that I take an interest in or just archiving, so unless optimization is the express purpose of the program, having it work as expected and not take 3.x billion years is usually enough for me.

For ImgToAscii just provide an image with "python ImgToAscii.py *image file*". for the code golfed version, the file needs to be supplied in the program itself.

## Inverse Kinematics

I was looking into procedural animation and came across a lot of interesting ideas with a lot of interesting applications. The main drawback I saw was that the approaches I saw tended to require a ton of computation to get right, and it only got more complex the more joints that got added into the system. I ended up looking into the Forward And Backward Reching Inverse Kinematics algorithm (FABRIK) and it looked simple enough to put together a prototype in an afternoon. Honestly, I can believe how realistic and complex the results appear for such a simple idea. Granted, I didn't do anything very impressive with this implementation, but the fact that I was able to get things up and working in such a short time is a massive credit to the creators of the algorithm. This is probably the shortest and least problematic project in this entire repo. Oh well, guess they can't all be horrible, torturous creatures that fight me in every step of their lifecycle. The coding gods must like me today.

## Magic Trick

Oddly enough, this little project started very small and stayed small. That doesn't happen very often, as I'm sure is made obvious by the other projects in this repo. I did dig into the math behind why the trick works but I figured that wasn't going to be interesting to show, so enjoy a simple toy to act out a magic trick I know.

## Marching Squares

I was inspired to look into marching cubes by Sebastian Lague's video on the topic, but I decided that my usual GUI approach wasn't going to work very well with 3D without doing a lot of work on a topic I'd already played with (see my graphics projects). Seeing as I was more interested in just getting my hands dirty and not reinventing the graphics wheel for the 1000th time (the classic thing programmers love to do for no reason... I'm not a hypocrite on that at all), I went for marching squares in 2D instead. Same concept, slightly easier math - an absolutely massive plus for me. While I was looking into the subject, I came across ray marching and signed distance functions, so maybe I'll go look at that if I ever come back around to this sort of area of study.

Seeing as I made this after making (stealing) my WFC program I figured a config file might be a nice idea. The Square and Circle files just contain the required code to get collision detection, movement, and implicit functions working for those specific shapes so that the actual driving program could be a lot more abstract. Technically, this approach works for any implicit function provided it has a way to be updated (even if that does nothing) and a way to return a value for the implicit function that describes it when handed a 2D point, but finding implicit functions for other polygons like triangles can be a lot more complicated than I'd like so the 2 shapes in this project are all I added.

Place all the files in the same directory and run MarchingSquaresVisual to get it going. Theres much less configuration on the fly than my other projects since a lot of it needed to be done up front and be immutable, sorry about that. Feel free to add your own shapes and see how they react

## Mouse Generator

This is just a little tool I made to generate characters for the Mausritter ttrpg system. There is are tools that exist to do this already, but I wanted something that I could extend for my own use as needed. The structure is a bit strange, but again I wanted it to be something I could adjust as needed without having to mess with the generation process too much.

Generate only makes 1 mouse at a time as I have it now, so if you want more at once you'd have to change that number yourself.

## Origin Shift

Recently, some friends and I got on a Minecraft kick. As always happens whenever Minecraft pulls me in again, I rediscovered the fun I have with designing redstone contraptions/ farms. While looking for new designs, I came across a maze generation algorithm that allows for the maze pathways to be shifted on the fly called Origin Shift which is covered here: https://youtu.be/zbXKcDVV4G0?si=0LRFJhmq3zOhsdRp.

The basic idea is that a 'good' maze has a few key properties: every cell in the grid can reach every other cell via some path and no loops are present in the pathways. We accomplish this by establishing the pathways of the maze as a root directed tree. Which is to say that every node points to one other node (except the origin) and all nodes are able to reach the origin following the pointers. As long as those properties are valid, the maze can shift where the origin is at will and adjust the cooresponding walls. Do this enough and you have a random looking maze. To make it more interesting, I added the ability to toggle vision on some of the components of the maze to see what they look like (including the solution to the maze)

Place all the files in the same directory and run MazeVisual to get this running. Note that the configs are in the MazeVisual file at the top of the code.

## Ray Marching

As I mentioned in my notes on the Marching Squares project, I did end up circling around to this topic eventually. Originally, I was planning on writing something in 3D with a python wrapper for OpenGL, but I ultimately decided to just do something simpler. CodeParade was where most of my understanding of this topic came from, and he used 2D visualizations to explain pieces of it so that's what I went with. Overall, not as complicated to make as I though it was going to be. Some serious credit for this goes to Inigo Quilez for his insane obsession with graphics (specifically his absolutely massive list of 2D primitive SDFs) as well as the many, many awesome videos explaining how this all works. CodeParade and Sebastian Lague were the 2 main people I watched, but there are a lot more than that. 

The actual code footprint is small enough that I could have put everything in 1 file, but I think this is much more digestable if it's loosely split up by concept. Ray is the actual ray march algorithm, Shapes is the list of SDFs I hard coded from the list I mentioned, March is the main driver, and Utils is just some config options and helpers. 

Keep everything in the same folder and run March to get it going.

## Sierpinski

I mostly uploaded this just because it was the first project I did at college, and it looks cool. No real other reason. Just enjoyed making it and thought to archive it. The code looks very hand-holdy and different to a lot of the other projects here because it was pretty much dictated line by line from a prof of mine.

## Splines

I often find myself in the mood to just build things and see if I can make it work as I imagine, and it was on one such occasion that I stumbled across De Casteljau's algorithm. I've never been one for pure math, so the visual aspect of what this algorithm described so beautifully interested me greatly. This led to a rabbit hole of video games, animation, vector graphics, and all sorts of other applications. Ultimately, I ended up implementing the BezierCurve file you see and liked how it looked so much I decided to see what else this thing could do. 

BezierSplines are just multiple curves stapled together, HermiteSplines supposedly use vectors to define tangents at the control points, but they secretly can be defined by specific implementations of BezierCurves, CardinalSplines are much the same except the vectors are automatically defined, and CatmullRomSplines are just a specific kind of CardinalSpline. All of this from one simple little algorithm... except LinearSplines. Those were just too funny to leave out.

Keep all the files in the same directory and run SplinesVisual for this one, and feel free to mess with the definitions of the splines individually.

## TicTacToe

This program came out of a truly idiotic conversation where I and some coworkers were discussing the idea that you could make anything if you just wrote enough if statements. Naturally, I wanted to see how far you could push that idea while still making something 'useful' and thus was this stupid thing born. The idea is that it pulls a list of possible board states (which I wrote manually) and the best possible move to make if it appears (which I also calculated and wrote manually) from a text file. It then stores that data and references it when needed instead of running fancy algoithms or any of that other smart nonsense. Not quite the if statement glory it could have been, but the idea is there: if this board state, then this move.

You will need both files in the same folder, or to change the file path if you run TicTacToe as is. Alternatively, you can implement the class and give it your own dictionary in the format of the original txt file.

## Verlet Physics

Physics simulations were something I thought comletely beyond my reach for a really long time and I've always wanted to make one, but I just never got over that mental barrier. Since starting this repo, I've played with a lot of topics I once thought too difficult to get into, so I figured it was time to finally see what I could throw together. I settled on Verlet Integration as the main source of the physics calculations because I wanted to focus on soft-body and cloth as the main targets of the project and other methods tended to do better for rigid-bodies instead. Honestly, I'm a little embarrassed I waited so long to do this. I had an absolute blast with this thing. I added some bells and whistles to the simulation to make the default cloth work better, but if you're willing to tweak the internal numbers a bit, you can get a surprising amount of functionality for other kinds of physics objects with such a simple implementation.

The basic idea is that everything is made of masses and springs. Rigid bodies have extremly stiff internal springs and soft bodies have the opposite. As long as everything is properly connected together, the springs can provide internal support, structure, and ensure that everything generally stays in one piece. Masses have an elasticity value to determine how much velocity is lost on collision with the environment and a mass to determine how much they are affected by forces. Springs connect two masses, have an ideal relaxed length, a compressability value to determine how quickly they correct stretching and commpressing, and finally a multiple of their length at which they will become strained and snap. I added the ability to set masses and springs on fire because one of my coworkers saw what I was working on and wanted to "Set it on fire just to see what would happen". That single, unsolicited, psychotic statement was too funny not to try and do.

Keep all the files in the same directory and run VerletVisual to see the cloth simulation. Flame particles can be very taxing if the ratio of spread chance to destroy chance is too imbalanced towards spreading - especially when the number of masses and springs is high as it would be for a small gridsize or high resolution. Tweaking the max number of particles spawned or the rate at which the particles disappear may be necesarry to get smooth performance in some cases.

## Voronoi

First discovery of this topic came when I was looking into triangulation algorithms for the GJK project and stumbled into Delauney Triangulation. It didn't turn out to be too terribly useful for me and I didn't even end up implementing any sort of triangulation in that program, but something stuck with me about it. I knew about Voronoi Diagrams, but they weren't too high on my list of interests - that is until I found out that the graphs the two form are actually duals of each other: one can directly be converted to the other and back. I hadn't messed with graph theory or anything of that nature outside of networking classes and such in college, so I figured it might be fun to see what I could get up to. All in all, I think I'm done messing with graphs for the forseeabale future. 

I initially tried to generate the Voronoi first and get the Delauney from that, but it turned out to be infinitely simpler for me to go the other way around since Fortune's algorithm was a little beyond me. Ultimately I ended up using the Bowyer-Watson algorithm for the triangulation and just converted using the circumcenters the mesh provided. I can't pretend that a lot of what I read about all of this didn't go whistling high over my head, but at least I had fun for the 2 days of pain this caused me. A lesson for future me then: do some preliminary research before you decide to jump head-first into a project on a topic you know next to nothing about, and all hail the gods of spaghetti code.

Keep all the files in the same directory and run VoronoiVisual for this one. Don't forget to play with the Config file to see what you can get.

## WFC

I first encountered the wave function collapse algorithm through the games of Oskar Stålberg. I was interested to see how the level generation was done and came across a YouTube video explaining WFC by Martin Donald and wanted to play with it myself. Since I was more interested in just having something to play with and not with spending many hours of my life fine tuning a tile set, I semi took the approach that the original implementation did and decided to allow it to generate its own rules and constrains based on an example image. Most of this code is taken from https://github.com/CodingQuest2023/Algorithms/tree/main/WorldGeneration/WaveFunctionCollapse so I could get things up and running quickly. The parts that allow for generation of the rules and such as well as the edits I made to fit those rules in the actual algorithm are my only real contribution here.

Some notes on the program in general: WFC works best when the number of ways to fail is very low, so try to provide examples with a relatively low number of unique tiles while still displaying a lot of possible permutations they can appear in. This program does recognize structures that take up more than 1 tile, but those structures have to be internally consistent and they may make failure more likely. The rules are not stored as connections but as pure references to what tiles can go where which can make failure rates higher if the example doesn't match well with that critera.

Config.py allows for some tweaking of the output, and it is where the path to the example image is specified. Make sure all python files are in the same directory and run WFC.py to get it working.