cmake_minimum_required( VERSION 3.15 )

message( STATUS "Parallel Programming Course" )
include(${CMAKE_SOURCE_DIR}/cmake/Configure.cmake)
############################### LATEX ###############################
option(USE_LATEX OFF)
if( USE_LATEX )
    if ( NOT APPLE )
        include( cmake/UseLATEX.cmake )
    else( NOT APPLE )
        set( USE_LATEX OFF )
    endif( NOT APPLE )
endif( USE_LATEX )

add_subdirectory(modules)
