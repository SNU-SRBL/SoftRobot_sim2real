#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Helper" for configuration "MinSizeRel"
set_property(TARGET Sofa.Helper APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Helper PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Helper.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Helper.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Helper )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Helper "${_IMPORT_PREFIX}/lib/Sofa.Helper.lib" "${_IMPORT_PREFIX}/bin/Sofa.Helper.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
