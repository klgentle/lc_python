package com.itranswarp.learnjava;

import java.io.IOException;
import java.math.BigInteger;

import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonDeserializer;

public class IsbnDeserializer extends JsonDeserializer<BigInteger> {

	@Override
	public BigInteger deserialize(JsonParser p, DeserializationContext ctxt)
			throws IOException, JsonProcessingException {
		String s = p.getValueAsString();
		if (s != null) {
			try {
				return new BigInteger(s.replace("-", ""));
			} catch (NumberFormatException e) {
				throw new JsonParseException(p, s, e);
			}
		}
		return null;
	}
}
