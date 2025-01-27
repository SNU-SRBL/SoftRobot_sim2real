#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.DefaultType" for configuration "MinSizeRel"
set_property(TARGET Sofa.DefaultType APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.DefaultType PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.DefaultType.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.DefaultType.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.DefaultType )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.DefaultType "${_IMPORT_PREFIX}/lib/Sofa.DefaultType.lib" "${_IMPORT_PREFIX}/bin/Sofa.DefaultType.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
