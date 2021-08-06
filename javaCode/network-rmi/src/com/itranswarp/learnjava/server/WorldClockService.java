package com.itranswarp.learnjava.server;

import java.rmi.RemoteException;
import java.time.LocalDateTime;
import java.time.ZoneId;

import com.itranswarp.learnjava.shared.WorldClock;

public class WorldClockService implements WorldClock {

	@Override
	public LocalDateTime getLocalDateTime(String zoneId) throws RemoteException {
		return LocalDateTime.now(ZoneId.of(zoneId)).withNano(0);
	}
}
