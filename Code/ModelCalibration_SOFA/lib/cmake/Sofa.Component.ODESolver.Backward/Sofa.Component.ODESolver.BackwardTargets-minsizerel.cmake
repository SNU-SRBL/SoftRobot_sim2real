#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.ODESolver.Backward" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.ODESolver.Backward APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.ODESolver.Backward PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.ODESolver.Backward.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.ODESolver.Backward.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.ODESolver.Backward )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.ODESolver.Backward "${_IMPORT_PREFIX}/lib/Sofa.Component.ODESolver.Backward.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.ODESolver.Backward.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
