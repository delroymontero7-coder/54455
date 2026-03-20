import unreal

def main():
    world = unreal.EditorLevelLibrary.get_editor_world()
    actor_location = unreal.Vector(0.0, 0.0, 200.0)
    actor_rotation = unreal.Rotator(0.0, 0.0, 0.0)
    actor = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.StaticMeshActor,
        actor_location,
        actor_rotation
    )
    if actor:
        actor.set_actor_label("Omni_Test_Actor")
        unreal.log("Actor de prueba creado correctamente.")
    else:
        unreal.log_error("No se pudo crear el actor de prueba.")

main()
