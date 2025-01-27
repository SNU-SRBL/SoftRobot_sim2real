#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaSparseSolver" for configuration "MinSizeRel"
set_property(TARGET SofaSparseSolver APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaSparseSolver PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaSparseSolver.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaSparseSolver.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaSparseSolver )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaSparseSolver "${_IMPORT_PREFIX}/lib/SofaSparseSolver.lib" "${_IMPORT_PREFIX}/bin/SofaSparseSolver.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
