import bpy
import random
possible_screws = 12
numberOfScrews = 10
bpy.context.scene.render.resolution_x = 500 #perhaps set resolution in code
bpy.context.scene.render.resolution_y = 500  
newcsv = open("trainfile.csv","w+")
screws = bpy.data.objects
cube = bpy.data.objects['Cube']
for loop in range(5):
    #initial locations outside the view angle
    for i in range(possible_screws):
         screws[i].location=(1.7,3,1)
    newcsv.write("train%d.png," %(loop))
    #cube is located at 0,0 with scale 1,1,0.3 extends from -1,1 in x and y 
    #range needs to be inside [-1,1] to be on the cube
    #select screws from the range 
    item_list = random.sample(range(possible_screws),numberOfScrews)
    #possible locations for screws
    coordinate_list=[]
    for i in range(-4,5):
        for j in range(-4,5):
            coordinate_list.append((i,j))
    k=0
    ##screw arrangement code here
    for i in item_list:
        k+=1
        names="bool "+str(k)
        #create 25 positions (first digit better not repeat)
        #create a 8x8 imaginary grid on the cube, random 2 numbers from -4 to 4 and add noise
        g = random.sample(coordinate_list,1)
        coordinate_list.remove(g[0])    
        x=g[0][0]*0.22 + (random.random()-0.5)* 0.07
        y=g[0][1]*0.22 + (random.random()-0.5)* 0.07
        #noise
        noise = (random.random()-0.5)* 0.1
        screws[i].location=(x,y,0.7)
        #move light to some position
        bool_one = cube.modifiers.new(type="BOOLEAN", name=names)
        bool_one.object = screws[i]
        bool_one.operation = 'DIFFERENCE'
        stringer = str((x+1)*250)+","+str((y+1)*250)+","+str(screws[i].name)
        newcsv.write(stringer)
        newcsv.write("\n")
    newcsv.write("\n")  
    #light position and angle
    x=random.random()*8 - 4
    y=random.random()*8 - 4
    z=4.17
    bpy.data.objects['Light'].location = (x,y,z)
    bpy.context.scene.render.filepath = '/home/pavithran/synthdata/train/train'+str(loop)+'.png'
    bpy.ops.render.render(animation=False, write_still=True, use_viewport=False, layer="", scene="")
    #bpy.ops.render.render()
    for k in range(numberOfScrews+1): 
        name ="bool "+str(k)
        bpy.ops.object.modifier_remove(modifier=name)
