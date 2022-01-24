#!/usr/bin/env python
import os, glob

from gimpfu import gimp
import gimpcolor

size_switcher = {
    0: (226, 226),
    1: (175, 175),
    2: (80, 80),
    3: (64, 64),
    4: (32, 32),
    5: (28, 434)
}
 
def process(in_name, out_name, type, button_state, is_circular):
    # if (os.path.exists(out_name)):
    #     print("Warning! Do you want to overwrite: " + out_name)
    #     yes = input()
    #     if input != "yes":
    #         return
    #print("in=%s,out=%s,type=%s,state=%s" % (in_name, out_name, type, button_state))
    #return
    if not in_name:
        print("Input file cannot be empty")
        return
    if not out_name:
        print("Output file cannot be empty")
        return
    if not out_name.endswith(".tga"):
        print("invalid output file format (use .tga)")
        return
    size = size_switcher.get(type)
    if size is None:
        print("invalid icon type")
        return
    
    if in_name.endswith(".svg"):
        image = gimp.pdb.file_svg_load(in_name, in_name, 90, size[0], size[1], 2)
    elif in_name.endswith(".xcf"):
        image = gimp.pdb.gimp_xcf_load(0, in_name, in_name)
        gimp.pdb.gimp_image_scale(image, size[0], size[1])
    else:
        print("invalid input file format")
        return

    if button_state == "up":
        image_up(image)
    elif button_state == "down":
        image_down(image)
    elif button_state == "over":
        image_over(image)
    elif button_state == None:
        pass
    else:
        print("invalid button state")
        return

    drawable = gimp.pdb.gimp_image_get_active_drawable(image)
    if is_circular:
        image_circular(drawable)

    gimp.pdb.file_tga_save(image, drawable, out_name, out_name, 0, 0)

def image_up(image):
    gimp.pdb.plug_in_lighting(image, gimp.pdb.gimp_image_get_active_drawable(image), None, None, 0, 0, 0, 0, gimpcolor.RGB(200,200,200), 0.5, -0.1, 0.6, 0.0, 0.0, 0.0, 1.2, 0.0, 0.0, 0.0, 0.0, 0, 0, 0)

def image_over(image):
    image_up(image)
    gimp.pdb.gimp_drawable_brightness_contrast(gimp.pdb.gimp_image_get_active_drawable(image), 0.27, 0)

def image_down(image):
    gimp.pdb.plug_in_lighting(image, gimp.pdb.gimp_image_get_active_drawable(image), None, None, 0, 0, 0, 0, gimpcolor.RGB(200,200,200), 0.5, 1.2, 0.6, 0.0, 0.0, 0.0, 1.2, 0.0, 0.0, 0.0, 0.0, 0, 0, 0)
    gimp.pdb.gimp_drawable_brightness_contrast(gimp.pdb.gimp_image_get_active_drawable(image), -0.27, 0)

def image_circular(drawable):
    image = drawable.image
    gimp.pdb.gimp_image_select_ellipse(image, 2, 0, 0, image.width, image.height)
    gimp.pdb.gimp_selection_invert(image)
    gimp.pdb.gimp_edit_bucket_fill(drawable, 0, 58, 100, 0, 0, 0, 0)

def run(directory, out_directory):
    print("using directory: " + os.path.abspath(directory))
    for infile in glob.glob(os.path.join(directory, 'Masteries', '**', 'masteryBar.*')):
        print("processing skillbar file: " + infile)
        infile, outfile, outfilename = handle_file(directory, out_directory, infile)

        #print(outfile)
        process(infile, outfile, 5, None, False)
    
    for infile in glob.glob(os.path.join(directory, 'Masteries', '**', 'masteryPlus*.*')):
        print("processing plus button file: " + infile)
        infile, outfile, outfilename = handle_file(directory, out_directory, infile)

        if "Up" in outfilename:
            process(infile, outfile, 3, "up", False)
            continue
        elif "Down" in outfilename:
            process(infile, outfile, 3, "down", False)
            continue
        process(infile, outfile.replace(outfilename, outfilename.replace('.', 'Up.')), 3, "up", False)
        process(infile, outfile.replace(outfilename, outfilename.replace('.', 'Down.')), 3, "down", False)
        
    for infile in glob.glob(os.path.join(directory, 'Masteries', '**', 'mastery.*')):
        print("processing mastery file: " + infile)
        infile, outfile, outfilename = handle_file(directory, out_directory, infile)

        process(infile, outfile.replace(outfilename, outfilename.replace('.', 'Preview.')), 0, None, True) # preview
        process(infile, outfile, 1, None, True) # mastery panel
        process(infile, outfile.replace(outfilename, outfilename.replace('.', 'ButtonUp.')), 2, "up", True) # mastery select button
        process(infile, outfile.replace(outfilename, outfilename.replace('.', 'ButtonDown.')), 2, "down", True) # mastery select button
        process(infile, outfile.replace(outfilename, outfilename.replace('.', 'ButtonOver.')), 2, "over", True) # mastery select button
        
    for infile in glob.glob(os.path.join(directory, 'Skills', '**', '*.svg')):
        print("processing skill file: " + infile)
        infile, outfile, outfilename = handle_file(directory, out_directory, infile)
        is_circular = "passive_" in infile
        outfile=outfile.replace("passive_", "").replace("active_", "")
        
        # if "Up" in outfilename or "Down" in outfilename or "Over" in outfilename:
        #     continue
        process(infile, outfile.replace(outfilename, outfilename.replace('.', 'Up.')), 4, "up", is_circular)
        process(infile, outfile.replace(outfilename, outfilename.replace('.', 'Down.')), 4, "down", is_circular)

def handle_file(directory, out_directory, infile):
    infile=os.path.abspath(infile)
    relative_path=os.path.relpath(infile, os.path.abspath(directory))
    outfile=os.path.abspath(os.path.join(out_directory, os.path.splitext(relative_path)[0] + ".tga"))
    #print(outfile)
    outfilename=os.path.basename(outfile)
    return infile,outfile,outfilename
