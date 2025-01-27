#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "libqpOASES" for configuration "MinSizeRel"
set_property(TARGET libqpOASES APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(libqpOASES PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/libqpOASES.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/libqpOASES.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS libqpOASES )
list(APPEND _IMPORT_CHECK_FILES_FOR_libqpOASES "${_IMPORT_PREFIX}/lib/libqpOASES.lib" "${_IMPORT_PREFIX}/bin/libqpOASES.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
