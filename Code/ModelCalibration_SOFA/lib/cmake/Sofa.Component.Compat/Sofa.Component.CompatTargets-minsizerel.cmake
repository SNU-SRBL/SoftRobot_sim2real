#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Compat" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Compat APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Compat PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Compat.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Compat.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Compat )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Compat "${_IMPORT_PREFIX}/lib/Sofa.Component.Compat.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Compat.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
