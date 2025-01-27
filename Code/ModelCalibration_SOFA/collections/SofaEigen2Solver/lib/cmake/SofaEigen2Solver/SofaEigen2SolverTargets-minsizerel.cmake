#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SofaEigen2Solver" for configuration "MinSizeRel"
set_property(TARGET SofaEigen2Solver APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(SofaEigen2Solver PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/SofaEigen2Solver.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/SofaEigen2Solver.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS SofaEigen2Solver )
list(APPEND _IMPORT_CHECK_FILES_FOR_SofaEigen2Solver "${_IMPORT_PREFIX}/lib/SofaEigen2Solver.lib" "${_IMPORT_PREFIX}/bin/SofaEigen2Solver.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
