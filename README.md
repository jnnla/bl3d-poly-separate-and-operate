# bl3d-poly-separate-and-operate

A python script for Blender that separates every polygon of a mesh and adds child nulls at each vertex.

DISCLAIMER: This is a utility script I created for a specific project and does a very specific thing. My hope is that sharing this will help others in some way. I don't claim to have any expertise and understanding of programming or code. I'm just experimenting and sometimes my experiments work.

This script was written and used in Blender 3.3. This script was intented to do a few things:

1) Take a mesh object and split out every single polygon into its own mesh.
2) Create null objects at every vertex of each separated polygon and parent those nulls to that polygon
3) 'Shrink' that separated polygon with an inset and delete the edge faces to create space between all the polys of the mesh. 
