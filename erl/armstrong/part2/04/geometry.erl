-module(geometry).
-export([area/1, perimeter/1]).

area({rectangle, Width, Height}) -> Width * Height;
area({circle, Radius}) -> 3.14159 * Radius * Radius;
area({triangle, Width, Height}) -> 1/2 * Width * Height;
area({square, Side}) -> Side * Side.

perimeter({rectangle, Width, Height}) -> 2 * Width * Height;
perimeter({circle, Radius}) -> 2 * 3.14159 * Radius;
perimeter({triangle, A, B, C}) -> A + B + C;
perimeter({square, Side}) -> 4 * Side.
