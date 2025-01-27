#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Simulation.Graph" for configuration "MinSizeRel"
set_property(TARGET Sofa.Simulation.Graph APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Simulation.Graph PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Simulation.Graph.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Simulation.Graph.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Simulation.Graph )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Simulation.Graph "${_IMPORT_PREFIX}/lib/Sofa.Simulation.Graph.lib" "${_IMPORT_PREFIX}/bin/Sofa.Simulation.Graph.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
