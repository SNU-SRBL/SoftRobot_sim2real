#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Compat" for configuration "MinSizeRel"
set_property(TARGET Sofa.Compat APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Compat PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Compat.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Compat.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Compat )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Compat "${_IMPORT_PREFIX}/lib/Sofa.Compat.lib" "${_IMPORT_PREFIX}/bin/Sofa.Compat.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
