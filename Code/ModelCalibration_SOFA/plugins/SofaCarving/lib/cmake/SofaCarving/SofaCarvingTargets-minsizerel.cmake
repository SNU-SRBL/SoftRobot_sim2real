#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaCarving" for configuration "MinSizeRel"
set_property(TARGET SofaCarving APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaCarving PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaCarving.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaCarving.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaCarving )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaCarving "${_IMPORT_PREFIX}/lib/SofaCarving.lib" "${_IMPORT_PREFIX}/bin/SofaCarving.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
