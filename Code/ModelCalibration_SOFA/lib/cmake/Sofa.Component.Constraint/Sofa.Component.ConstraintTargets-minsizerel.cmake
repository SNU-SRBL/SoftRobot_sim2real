#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Constraint" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Constraint APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Constraint PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Constraint.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Constraint.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Constraint )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Constraint "${_IMPORT_PREFIX}/lib/Sofa.Component.Constraint.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Constraint.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
