#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Diffusion" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Diffusion APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Diffusion PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Diffusion.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Diffusion.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Diffusion )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Diffusion "${_IMPORT_PREFIX}/lib/Sofa.Component.Diffusion.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Diffusion.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
