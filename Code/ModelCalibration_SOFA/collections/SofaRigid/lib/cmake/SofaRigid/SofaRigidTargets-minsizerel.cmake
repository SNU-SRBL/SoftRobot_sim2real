#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaRigid" for configuration "MinSizeRel"
set_property(TARGET SofaRigid APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaRigid PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaRigid.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaRigid.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaRigid )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaRigid "${_IMPORT_PREFIX}/lib/SofaRigid.lib" "${_IMPORT_PREFIX}/bin/SofaRigid.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
