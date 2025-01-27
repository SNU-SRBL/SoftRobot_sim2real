#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.ODESolver" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.ODESolver APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.ODESolver PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.ODESolver.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.ODESolver.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.ODESolver )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.ODESolver "${_IMPORT_PREFIX}/lib/Sofa.Component.ODESolver.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.ODESolver.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
