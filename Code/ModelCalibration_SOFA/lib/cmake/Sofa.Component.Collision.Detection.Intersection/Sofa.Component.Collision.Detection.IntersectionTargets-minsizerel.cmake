#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Sofa.Component.Collision.Detection.Intersection" for configuration "MinSizeRel"
set_property(TARGET Sofa.Component.Collision.Detection.Intersection APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(Sofa.Component.Collision.Detection.Intersection PROPERTIES
  IMPORTED_IMPLIB_MINSIZEREL "${_IMPORT_PREFIX}/lib/Sofa.Component.Collision.Detection.Intersection.lib"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/bin/Sofa.Component.Collision.Detection.Intersection.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Sofa.Component.Collision.Detection.Intersection )
list(APPEND _IMPORT_CHECK_FILES_FOR_Sofa.Component.Collision.Detection.Intersection "${_IMPORT_PREFIX}/lib/Sofa.Component.Collision.Detection.Intersection.lib" "${_IMPORT_PREFIX}/bin/Sofa.Component.Collision.Detection.Intersection.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
