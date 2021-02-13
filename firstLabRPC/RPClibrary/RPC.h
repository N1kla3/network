//
// Created by nicola on 10/02/2021.
//
#pragma once

#include <boost/log/core.hpp>
#include <boost/log/expressions.hpp>
#include <boost/log/sinks/text_file_backend.hpp>
#include <boost/log/sources/record_ostream.hpp>
#include <boost/log/sources/severity_logger.hpp>
#include <boost/log/trivial.hpp>
#include <boost/log/utility/setup/common_attributes.hpp>
#include <boost/log/utility/setup/console.hpp>
#include <boost/log/utility/setup/file.hpp>

namespace logging = boost::log;
namespace src = boost::log::sources;
namespace sinks = boost::log::sinks;
namespace keywords = boost::log::keywords;

src::severity_logger<logging::trivial::severity_level> lg;

void InitLog()
{
    logging::add_file_log(keywords::file_name = "sample%N.log", keywords::rotation_size = 10 * 1024 * 1024,
                          keywords::time_based_rotation = sinks::file::rotation_at_time_point(0, 0, 0),
                          keywords::format = "[%TimeStamp%]<%Severity%>: %Message%");

    logging::add_console_log(std::cout, boost::log::keywords::format = "<%Severity%> %Message%");
    logging::add_common_attributes();
}


#define LOG_TRACE(text) BOOST_LOG_SEV(lg, logging::trivial::trace) << #text
#define LOG_DEBUG(text) BOOST_LOG_SEV(lg, logging::trivial::debug) << #text
#define LOG_INFO(text)  BOOST_LOG_SEV(lg, logging::trivial::info) << #text
#define LOG_WARNING(text) BOOST_LOG_SEV(lg, logging::trivial::warning) << #text
#define LOG_ERROR(text) BOOST_LOG_SEV(lg, logging::trivial::error) << #text
#define LOG_FATAL(text) BOOST_LOG_SEV(lg, flogging::trivial::atal) << #text