#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Topology.Container.Dynamic" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Topology.Container.Dynamic APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Topology.Container.Dynamic PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Topology.Container.Dynamic.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Topology.Container.Dynamic.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Topology.Container.Dynamic )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Topology.Container.Dynamic "${_IMPORT_PREFIX}/lib/Sofa.Component.Topology.Container.Dynamic.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Topology.Container.Dynamic.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
