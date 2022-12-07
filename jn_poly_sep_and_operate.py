import bpy

#define selection as active object:
sel = bpy.context.active_object

#Get polyCount of active object:
polyCount = len(sel.data.polygons.values())

#loop downwards from top of polycount:
for n in range(polyCount-1,0,-1):
    
    #select original selection
    sel.select_set(True)
    
    #deselect all faces in edit mode
    bpy.ops.object.mode_set(mode = 'EDIT') 
    bpy.ops.mesh.select_mode(type="FACE")
    bpy.ops.mesh.select_all(action = 'DESELECT')

    #return to object mode to select polygon by index, then flip to edit to see selection.
    bpy.ops.object.mode_set(mode = 'OBJECT')
    sel.data.polygons[n].select = True
    bpy.ops.object.mode_set(mode = 'EDIT') 

    #Separate the selected polygon:
    bpy.ops.mesh.separate(type='SELECTED')

    #isolate the separated polygon:
    bpy.ops.object.mode_set(mode = 'OBJECT')
    split =  bpy.context.selected_objects.pop()
    bpy.ops.object.select_all(action='DESELECT') #deselect all

    #make separated polygon active:
    split.select_set(True)
    bpy.context.view_layer.objects.active = split

    # Create a null object for each vertex
    splitMesh = bpy.context.object.data
    for vertex in splitMesh.vertices:
        null = bpy.data.objects.new("Null", None)
        null.empty_display_size = 0.05
        null.location = vertex.co
        null.parent = split
        bpy.context.collection.objects.link(null)

    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.select_all(action='SELECT')

    #inset and delete edge faces
    bpy.ops.mesh.inset(thickness=0.000525, depth=0)
    bpy.ops.mesh.select_all(action='INVERT')
    bpy.ops.mesh.delete(type='FACE')

    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.object.select_all(action='DESELECT') #deselect all