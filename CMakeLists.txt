cmake_minimum_required( VERSION 3.13 )

message( STATUS "Programming Course Reports" )

include(${CMAKE_SOURCE_DIR}/cmake/Configure.cmake)

############################### LATEX ###############################
option(USE_LATEX OFF)
if( USE_LATEX )
    find_package(Python3 REQUIRED)
    set(LATEX_BIN_PATH "${CMAKE_BINARY_DIR}/bin/")
    if( NOT EXISTS ${LATEX_BIN_PATH} )
        file( MAKE_DIRECTORY ${LATEX_BIN_PATH} )
    endif( NOT EXISTS ${LATEX_BIN_PATH} )
endif( USE_LATEX )

add_subdirectory(modules)
