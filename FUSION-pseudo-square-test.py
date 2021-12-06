
import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Hello script')


        # Create a document.
        doc = app.documents.add(
            adsk.core.DocumentTypes.FusionDesignDocumentType)
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design
        rootComp = design.rootComponent

        # Get extrude features
        extrudes = rootComp.features.extrudeFeatures
        # Create sketch
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xYConstructionPlane)





####################################################################
# ^ above is preamble
#Create sketch of rectangular baseplate
        sketch = sketches.add(rootComp.xYConstructionPlane)
        #sketches.add(rootComp.xYConstructionPlane)
        #sketch = sketches.add(xyPlane)
        lines = sketch.sketchCurves.sketchLines

        #total widths of this pseudo square is 7"
        #psuedo corners are a 45 45 90 triangle with 1" sides
        point0 = adsk.core.Point3D.create(-6, 0, 0)
        point1 = adsk.core.Point3D.create(-7, 1, 0)
        point2 = adsk.core.Point3D.create(-7, 14, 0)
        point3 = adsk.core.Point3D.create(-6, 15, 0)

        point4 = adsk.core.Point3D.create(6, 15, 0)
        point5 = adsk.core.Point3D.create(7, 14, 0)
        point6 = adsk.core.Point3D.create(7, 1, 0)
        point7 = adsk.core.Point3D.create(6, 0, 0)
        lines.addByTwoPoints(point0, point1)
        lines.addByTwoPoints(point1, point2)
        lines.addByTwoPoints(point2, point3)
        lines.addByTwoPoints(point3, point4)
        lines.addByTwoPoints(point4, point5)
        lines.addByTwoPoints(point5, point6)
        lines.addByTwoPoints(point6, point7)
        lines.addByTwoPoints(point7, point0)
        prof = sketch.profiles.item(0)   
        profVertical = sketch.profiles.item(0)

        
        # # Extrude rectangle
        # distance = adsk.core.ValueInput.createByReal(0.2)
        # extrude1 = extrudes.addSimple(
        #     prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # # Get the extrusion body
        # body1 = extrude1.bodies.item(0)
        # body1.name = "simple"

        # # Get the state of the extrusion
        # health = extrude1.healthState
        # if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
        #     message = extrude1.errorOrWarningMessage

        # # Get the state of timeline object
        # timeline = design.timeline
        # timelineObj = timeline.item(timeline.count - 1)
        # health = timelineObj.healthState
        # message = timelineObj.errorOrWarningMessage





    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
