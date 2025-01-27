#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.ODESolver.Forward" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.ODESolver.Forward APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.ODESolver.Forward PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.ODESolver.Forward.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.ODESolver.Forward.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.ODESolver.Forward )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.ODESolver.Forward "${_IMPORT_PREFIX}/lib/Sofa.Component.ODESolver.Forward.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.ODESolver.Forward.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
