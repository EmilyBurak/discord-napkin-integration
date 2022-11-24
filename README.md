# Napkin Discord Integration Bot

This repo is the start of a Discord bot meant to integrate with [Napkin](https://www.napkin.one/), a fantastic note-taking app that makes collecting and linking ideas really fun. I highly recommend checking it out. Coded by [Emily Burak](emilytburak.com), best reached at emily@emilytburak.com

## Pre-requisites

- [Docker](https://docs.docker.com/)
- Populated .env file(see below.)
- Set up the bot on Discord's Developer Portal(plenty of tutorials for this one out there.)

## Installation

`docker build -t napkin-integration .`

` docker run -d --rm napkin-integration`
for now.

## Environment Variables

- Populate a `.env` file in the root directory with the following environment variables:

  > TOKEN={Your Discord Token}

  > EMAIL={Your Napkin email}

  > NAPKIN_TOKEN={Your Napkin API Token}

## Usage

DM the bot your thought! It'll post to Napkin with magic tags. The API is only meant for single thoughts, so don't spam it or you'll hit timeouts.

## Coming soon

- Fix discord.ext.commands.errors.CommandNotFound: Command `first argument of direct message` is not found / Ignoring exception in command None
- Implement !napkinhelp
- Pin requests version
- Tidy up everything
