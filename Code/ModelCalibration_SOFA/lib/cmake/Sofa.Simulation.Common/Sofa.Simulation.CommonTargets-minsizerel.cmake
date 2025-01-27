#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Simulation.Common" for configuration "MinSizeRel"
set_property(TARGET Sofa.Simulation.Common APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Simulation.Common PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Simulation.Common.lib"
  IMPORTED_LINK_DEPENDENT_LIBRARIES_MINSIZEREL "tinyxml"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Simulation.Common.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Simulation.Common )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Simulation.Common "${_IMPORT_PREFIX}/lib/Sofa.Simulation.Common.lib" "${_IMPORT_PREFIX}/bin/Sofa.Simulation.Common.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
