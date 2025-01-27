#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Testing" for configuration "MinSizeRel"
set_property(TARGET Sofa.Testing APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Testing PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Testing.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Testing.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Testing )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Testing "${_IMPORT_PREFIX}/lib/Sofa.Testing.lib" "${_IMPORT_PREFIX}/bin/Sofa.Testing.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
