<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <!-- ebb: This is going to mulan-xsl-out-1.xmlbe an identity transformation over a minimally-tagged XML file for a movie script.
    The xsl:mode element marks this as a simple identity transform: XML to XML where we make changes to the existing code. 
    Here is an excellent tutorial on how to write xsl:analyze-string: http://dh.obdurodon.org/analyze-string.xhtml 
    -->
    
     <!--Mulan Analyze String - EL Edition-->
     
     
    <xsl:mode on-no-match="shallow-copy"/>
    
    
    <!-- ebb: Here we are going to match on the elements we've marked and look for regex patterns inside them using a special XSLT function called xsl:analyze-string.
    -->
    <xsl:template match="text()">
        <xsl:analyze-string select="." regex="\[(.+?)\]" flags="s">
            <!-- @flags="s" sets the "dot matches all" functionality in xsl:analyze-string. Remove it if you need to prevent the dot from matching newline characters. -->
            <xsl:matching-substring>
                <info><xsl:value-of select="regex-group(1)"/></info>
            </xsl:matching-substring>
  
            <xsl:non-matching-substring>
                <xsl:apply-templates select="."/>
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>
    
    <xsl:template match="text()">
    <xsl:analyze-string select="." regex="^([A-Za-z].+):" flags="s">
        <xsl:matching-substring>
            <char><xsl:value-of select="regex-group(1)"/></char>
        </xsl:matching-substring>
        <xsl:non-matching-substring>
            <xsl:value-of select="."/>
        </xsl:non-matching-substring>
    </xsl:analyze-string>
    </xsl:template>
    
    <!--Matches to lines that begin with a string of capital or lowercase characters (names) followed by a colon, and wraps those pieces in "char" tags. - EL-->
    
    <!--<xsl:template match="sp">
        <xsl:analyze-string select="." regex="^\[(.+?)\]" flags="s">
            <xsl:matching-substring>
                <desc>[<xsl:value-of select="regex-group(1)"/>]</desc>
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="."/>
            </xsl:non-matching-substring>
        </xsl:analyze-string>
    </xsl:template>-->
    
<!--    This is my current prototype for identifying non-speech text/descriptions by finding something that starts immediately with a bracket and simply has stuff until there's another bracket. My problem is with figuring out the exact syntax and combining all three pieces together cohesively where one task is not trying to jump over the other. - EL-->
    
</xsl:stylesheet>

    