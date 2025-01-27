#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Constraint.Lagrangian.Correction" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Constraint.Lagrangian.Correction APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Constraint.Lagrangian.Correction PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Constraint.Lagrangian.Correction.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Constraint.Lagrangian.Correction.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Constraint.Lagrangian.Correction )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Constraint.Lagrangian.Correction "${_IMPORT_PREFIX}/lib/Sofa.Component.Constraint.Lagrangian.Correction.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Constraint.Lagrangian.Correction.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
