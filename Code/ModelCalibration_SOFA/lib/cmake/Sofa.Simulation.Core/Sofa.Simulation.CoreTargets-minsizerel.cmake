#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Simulation.Core" for configuration "MinSizeRel"
set_property(TARGET Sofa.Simulation.Core APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Simulation.Core PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Simulation.Core.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Simulation.Core.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Simulation.Core )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Simulation.Core "${_IMPORT_PREFIX}/lib/Sofa.Simulation.Core.lib" "${_IMPORT_PREFIX}/bin/Sofa.Simulation.Core.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
