#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaNonUniformFem" for configuration "MinSizeRel"
set_property(TARGET SofaNonUniformFem APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaNonUniformFem PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaNonUniformFem.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaNonUniformFem.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaNonUniformFem )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaNonUniformFem "${_IMPORT_PREFIX}/lib/SofaNonUniformFem.lib" "${_IMPORT_PREFIX}/bin/SofaNonUniformFem.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
