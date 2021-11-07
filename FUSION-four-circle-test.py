import adsk.core, adsk.fusion, adsk.cam, traceback


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Create a document.
        doc = app.documents.add(
            adsk.core.DocumentTypes.FusionDesignDocumentType)


        # change the file name here, place the parameters excel sheet to read values automatically
        f = open("C:/Users/Andrew Hu/Dropbox/PC/Downloads/cadparams-Modules.csv", "r")
        line = f.readline()
        data = [0,0,0]

        for i in range(0,3):
            pntStrArr = line.split(',')
            for pntStr in pntStrArr:
                data.append( str(pntStr))
                #x = data[0]
                y = data[1]
                z = data[2]

        width = float(data[4])
        cellthick = float(data[5])
        length = float(data[6])
        #########################################################
        # enter all values below in mm
        #cellthick = u
        #width = x
        #length = 155

        radius = 0.15 #radius in cm for 3mm diameter want 0.15cm
        #+1 in the cell thickness is to account for the 10mm thickness that the base plate has
        #the offset, in cm, is how much space you want to give the cells between the 8 posts
        height = (cellthick/10)*140+0.2
        cellwidth = width/10
        celllength = length/10
        offset = 0.2

        #########################################################
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design
        rootComp = design.rootComponent

        # Get extrude features
        extrudes = rootComp.features.extrudeFeatures
        # Create sketch
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xYConstructionPlane)

        #########
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(cellwidth/2, celllength/2+offset, 0)
        circle = sketchCircles.addByCenterRadius(centerPoint, radius)
 # Get the profile defined by the circle
        prof = sketch.profiles.item(0)

        # Extrude circle
        distance = adsk.core.ValueInput.createByReal(height)
        extrude1 = extrudes.addSimple(
            prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Get the extrusion body
        body1 = extrude1.bodies.item(0)
        body1.name = "simple"

        # Get the state of the extrusion
        health = extrude1.healthState
        if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
            message = extrude1.errorOrWarningMessage

        # Get the state of timeline object
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1)
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage







# Create sketch of rectangular baseplate
        sketch = sketches.add(rootComp.xYConstructionPlane)
#        sketches.add(rootComp.xYConstructionPlane)
        #sketch = sketches.add(xyPlane)
        lines = sketch.sketchCurves.sketchLines
        point0 = adsk.core.Point3D.create(-4, -17.4, 0)
        point1 = adsk.core.Point3D.create(-4, 17.4, 0)
        point2 = adsk.core.Point3D.create(4, 17.4, 0)
        point3 = adsk.core.Point3D.create(4, -17.4, 0)
        lines.addByTwoPoints(point0, point1)
        lines.addByTwoPoints(point1, point2)
        lines.addByTwoPoints(point2, point3)
        lines.addByTwoPoints(point3, point0)
        prof = sketch.profiles.item(0)
        profVertical = sketch.profiles.item(0)

        # Extrude rectangle
        distance = adsk.core.ValueInput.createByReal(0.2)
        extrude1 = extrudes.addSimple(
            prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Get the extrusion body
        body1 = extrude1.bodies.item(0)
        body1.name = "simple"

        # Get the state of the extrusion
        health = extrude1.healthState
        if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
            message = extrude1.errorOrWarningMessage

        # Get the state of timeline object
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1)
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage










 # Create sketch of second circle
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xYConstructionPlane)

        #########
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(-cellwidth/2, celllength/2+offset , 0)
        circle = sketchCircles.addByCenterRadius(centerPoint, radius)
        prof = sketch.profiles.item(0)

# Get the profile defined by the vertical circle
        profVertical = sketch.profiles.item(0)

        # Extrude second circle
        distance = adsk.core.ValueInput.createByReal(height)
        extrude1 = extrudes.addSimple(
            prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Get the extrusion body
        body1 = extrude1.bodies.item(0)
        body1.name = "simple"

        # Get the state of the extrusion
        health = extrude1.healthState
        if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
            message = extrude1.errorOrWarningMessage

        # Get the state of timeline object
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1)
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage








 # Create sketch of third circle
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xYConstructionPlane)

        #########
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(-cellwidth/2, -celllength/2-offset, 0)
        circle = sketchCircles.addByCenterRadius(centerPoint, radius)
        prof = sketch.profiles.item(0)

# Get the profile defined by the vertical circle
        profVertical = sketch.profiles.item(0)

        # Extrude third circle
        distance = adsk.core.ValueInput.createByReal(height)
        extrude1 = extrudes.addSimple(
            prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Get the extrusion body
        body1 = extrude1.bodies.item(0)
        body1.name = "simple"

        # Get the state of the extrusion
        health = extrude1.healthState
        if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
            message = extrude1.errorOrWarningMessage

        # Get the state of timeline object
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1)
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage






 # Create sketch of fourth circle
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xYConstructionPlane)

        #########
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(cellwidth/2, -celllength/2-offset, 0)
        circle = sketchCircles.addByCenterRadius(centerPoint, radius)
        prof = sketch.profiles.item(0)

# Get the profile defined by the vertical circle
        profVertical = sketch.profiles.item(0)

        # Extrude fourth circle
        distance = adsk.core.ValueInput.createByReal(height)
        extrude1 = extrudes.addSimple(
            prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Get the extrusion body
        body1 = extrude1.bodies.item(0)
        body1.name = "simple"

        # Get the state of the extrusion
        health = extrude1.healthState
        if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
            message = extrude1.errorOrWarningMessage

        # Get the state of timeline object
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1)
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage





















 # Create sketch of set2 - first circle
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xYConstructionPlane)

        #########
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(cellwidth/2+offset, celllength/2, 0)
        circle = sketchCircles.addByCenterRadius(centerPoint, radius)
        prof = sketch.profiles.item(0)

# Get the profile defined by the vertical circle
        profVertical = sketch.profiles.item(0)

        # Extrude first circle
        distance = adsk.core.ValueInput.createByReal(height)
        extrude1 = extrudes.addSimple(
            prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Get the extrusion body
        body1 = extrude1.bodies.item(0)
        body1.name = "simple"

        # Get the state of the extrusion
        health = extrude1.healthState
        if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
            message = extrude1.errorOrWarningMessage
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1)
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage

# Create sketch of set2 - second circle
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xYConstructionPlane)

        #########
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(-cellwidth/2-offset, celllength/2, 0)
        circle = sketchCircles.addByCenterRadius(centerPoint, radius)
        prof = sketch.profiles.item(0)

# Get the profile defined by the vertical circle
        profVertical = sketch.profiles.item(0)

        # Extrude second circle
        distance = adsk.core.ValueInput.createByReal(height)
        extrude1 = extrudes.addSimple(
            prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Get the extrusion body
        body1 = extrude1.bodies.item(0)
        body1.name = "simple"

        # Get the state of the extrusion
        health = extrude1.healthState
        if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
            message = extrude1.errorOrWarningMessage
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1)
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage

# Create sketch of set2 - third circle
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xYConstructionPlane)

        #########
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(cellwidth/2+offset, -celllength/2, 0)
        circle = sketchCircles.addByCenterRadius(centerPoint, radius)
        prof = sketch.profiles.item(0)

# Get the profile defined by the vertical circle
        profVertical = sketch.profiles.item(0)

        # Extrude third circle
        distance = adsk.core.ValueInput.createByReal(height)
        extrude1 = extrudes.addSimple(
            prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Get the extrusion body
        body1 = extrude1.bodies.item(0)
        body1.name = "simple"

        # Get the state of the extrusion
        health = extrude1.healthState
        if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
            message = extrude1.errorOrWarningMessage
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1)
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage

# Create sketch of set2 - fourth circle
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xYConstructionPlane)

        #########
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(-cellwidth/2-offset, -celllength/2, 0)
        circle = sketchCircles.addByCenterRadius(centerPoint, radius)
        prof = sketch.profiles.item(0)

# Get the profile defined by the vertical circle
        profVertical = sketch.profiles.item(0)

        # Extrude fourth circle
        distance = adsk.core.ValueInput.createByReal(height)
        extrude1 = extrudes.addSimple(
            prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Get the extrusion body
        body1 = extrude1.bodies.item(0)
        body1.name = "simple"

        # Get the state of the extrusion
        health = extrude1.healthState
        if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
            message = extrude1.errorOrWarningMessage
        timeline = design.timeline
        timelineObj = timeline.item(timeline.count - 1)
        health = timelineObj.healthState
        message = timelineObj.errorOrWarningMessage












        sketch = sketches.add(rootComp.xYConstructionPlane)
#        sketches.add(rootComp.xYConstructionPlane)
        #sketch = sketches.add(xyPlane)
        lines = sketch.sketchCurves.sketchLines
        point0 = adsk.core.Point3D.create(-cellwidth/2, -celllength/2, 0)
        point1 = adsk.core.Point3D.create(-cellwidth/2, celllength/2, 0)
        point2 = adsk.core.Point3D.create(cellwidth/2, celllength/2, 0)
        point3 = adsk.core.Point3D.create(cellwidth/2, -celllength/2, 0)
        lines.addByTwoPoints(point0, point1)
        lines.addByTwoPoints(point1, point2)
        lines.addByTwoPoints(point2, point3)
        lines.addByTwoPoints(point3, point0)
        prof = sketch.profiles.item(0)
        profVertical = sketch.profiles.item(0)



    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
