<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        
        <xsl:variable name="function"  select="button/function"/>
        <xsl:variable name="color"  select="button/color"/>
        
        <button class="btn btn-{$color} btn-sm mt-4" onclick="{$function}(event)">
            <xsl:value-of select="button/value" />
        </button>
        &#160;&#160;
        
    </xsl:template>
</xsl:stylesheet>
